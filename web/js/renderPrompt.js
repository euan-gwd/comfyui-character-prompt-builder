// Based on original code by pysssss (https://github.com/pysssss/comfyui-show-text)
// Forked in 2026

import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

// Displays input text on a node

// TODO: This should need to be so complicated. Refactor at some point.

function markDirty() {
	app?.graph?.setDirtyCanvas?.(true, false);
}

function normalizeTextPayload(text) {
	if (text == null) {
		return [];
	}

	// Older executions can send a plain string; newer frontend commonly sends arrays.
	if (typeof text === "string") {
		return [text];
	}

	if (!Array.isArray(text)) {
		return [[String(text)]];
	}

	const normalized = [];
	for (const entry of text) {
		if (entry == null || entry === "") {
			continue;
		}
		normalized.push(Array.isArray(entry) ? entry : [entry]);
	}
	return normalized;
}

app.registerExtension({
	name: "CharacterPromptBuilder.RenderPrompt",
	async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (nodeData.name === "renderPrompt") {
			function populate(text) {
				if (this.widgets) {
					// On older frontend versions there is a hidden converted-widget
					const isConvertedWidget = +!!this.inputs?.[0].widget;
					for (let i = isConvertedWidget; i < this.widgets.length; i++) {
						this.widgets[i].onRemove?.();
					}
					this.widgets.length = isConvertedWidget;
				}

				for (const list of normalizeTextPayload(text)) {
					for (const item of list) {
						const widgetName = "text_" + (this.widgets?.length ?? 0);
						const w = ComfyWidgets["STRING"](this, widgetName, ["STRING", { multiline: true }], app).widget;
						w.inputEl.style.opacity = 0.6;
						w.value = String(item);

						// Add event listener to update node's widgets_values
						w.inputEl.onchange = (function (node, widgetIndex) {
							return function (e) {
								if (!node.widgets_values) {
									node.widgets_values = [];
								}
								node.widgets_values[widgetIndex] = e.target.value;
								markDirty();
							};
						})(this, this.widgets.length - 1); // Pass 'this' (node) and the current widget index
					}
				}

				requestAnimationFrame(() => {
					const sz = this.computeSize();
					if (sz[0] < this.size[0]) {
						sz[0] = this.size[0];
					}
					if (sz[1] < this.size[1]) {
						sz[1] = this.size[1];
					}
					this.onResize?.(sz);
					markDirty();
				});
			}

			// When the node is executed we will be sent the input text, display this in the widget
			const onExecuted = nodeType.prototype.onExecuted;
			nodeType.prototype.onExecuted = function (message) {
				onExecuted?.apply(this, arguments);
				if (message.ui?.last_input) {
					if (!this.properties) {
						this.properties = {};
					}
					this.properties.last_input = message.ui.last_input[0];
				}
				const executionText = message.ui?.text ?? message.text ?? [];
				populate.call(this, executionText);
			};

			const VALUES = Symbol();
			const configure = nodeType.prototype.configure;
			nodeType.prototype.configure = function () {
				// Store unmodified widget values as they get removed on configure by new frontend
				this[VALUES] = arguments[0]?.widgets_values;
				return configure?.apply(this, arguments);
			};

			const onConfigure = nodeType.prototype.onConfigure;
			nodeType.prototype.onConfigure = function () {
				onConfigure?.apply(this, arguments);
				const widgets_values = this[VALUES];
				if (widgets_values?.length) {
					// In newer frontend there seems to be a delay in creating the initial widget
					requestAnimationFrame(() => {
						populate.call(this, widgets_values.slice(+(widgets_values.length > 1 && this.inputs?.[0].widget)));
					});
				}
			};
		}
	},
});