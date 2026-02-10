# Module-level cache to persist state across executions
_node_state_cache = {}


class RenderPrompt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "CharacterPromptBuilder"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        # Default to the input text
        current_input = (
            text[0]
            if isinstance(text, list) and len(text) > 0
            else (text if text is not None else "")
        )

        # Get node id
        node_id_str = None
        if unique_id is not None:
            node_id = (
                unique_id[0]
                if isinstance(unique_id, list) and len(unique_id) > 0
                else unique_id
            )
            node_id_str = str(node_id)

        # Get cached state for this node
        global _node_state_cache
        cached_state = _node_state_cache.get(node_id_str, {}) if node_id_str else {}
        cached_input = cached_state.get("last_input")
        cached_widget = cached_state.get("last_widget")

        # Determine what to output
        text_to_display = current_input

        if node_id_str and extra_pnginfo is not None:
            if isinstance(extra_pnginfo, list) and extra_pnginfo:
                workflow = extra_pnginfo[0].get("workflow")
                if workflow and "nodes" in workflow:
                    node = next(
                        (x for x in workflow["nodes"] if str(x["id"]) == node_id_str),
                        None,
                    )

                    if node:
                        # Get widget value from node
                        widget_value = None
                        if (
                            "widgets_values" in node
                            and isinstance(node["widgets_values"], list)
                            and len(node["widgets_values"]) > 0
                        ):
                            widget_value = node["widgets_values"][0]

                        # Logic:
                        # If input changed, use new input
                        # If input same but widget changed (and differs from input), it's a user edit - preserve it
                        # If input same and widget same as before, reset to input

                        if cached_input is None:
                            # First run - use input
                            text_to_display = current_input
                        elif cached_input != current_input:
                            # Input changed - use new input
                            text_to_display = current_input
                        elif widget_value is not None and widget_value != current_input:
                            # Input same, check if widget is a NEW edit
                            if cached_widget is None or widget_value != cached_widget:
                                # Widget value changed from last time - user made a new edit
                                text_to_display = widget_value
                            else:
                                # Widget is same as last time - user just reran, reset to input
                                text_to_display = current_input
                        else:
                            # Widget matches input or is None - use input
                            text_to_display = current_input

                        # Update the node's widgets_values to match our output
                        node["widgets_values"] = [text_to_display]

        # Cache the current input and widget for next time
        if node_id_str:
            _node_state_cache[node_id_str] = {
                "last_input": current_input,
                "last_widget": text_to_display,
            }

        return {
            "ui": {"text": [text_to_display]},
            "result": (),
        }


NODE_CLASS_MAPPINGS = {
    "renderPrompt": RenderPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "renderPrompt": "Character Prompt Builder - Render Prompt",
}
