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
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)

    CATEGORY = "CharacterPromptBuilder"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        # Default to the input text
        current_input = text[0] if isinstance(text, list) and len(text) > 0 else (text if text is not None else "")
        text_to_display = current_input

        if unique_id is not None and extra_pnginfo is not None:
            if isinstance(extra_pnginfo, list) and extra_pnginfo:
                workflow = extra_pnginfo[0].get("workflow")
                if workflow and "nodes" in workflow:
                    node_id = unique_id[0] if isinstance(unique_id, list) and len(unique_id) > 0 else unique_id
                    node_id_str = str(node_id)
                    node = next((x for x in workflow["nodes"] if str(x["id"]) == node_id_str), None)
                    
                    if node:
                        # Use properties to store the last seen input to detect changes
                        properties = node.get("properties", {})
                        last_input = properties.get("last_input")
                        
                        # If input has changed, it's the source of truth - replace any edits
                        if last_input != current_input:
                            text_to_display = current_input
                            # Update widgets_values to match the new source of truth
                            node["widgets_values"] = [text_to_display]
                        else:
                            # Input hasn't changed, so we can use existing edits if they exist
                            if "widgets_values" in node and isinstance(node["widgets_values"], list) and node["widgets_values"]:
                                text_to_display = node["widgets_values"][0]
                            else:
                                text_to_display = current_input
                                node["widgets_values"] = [text_to_display]
        
        # We send last_input in the UI message so the frontend can persist it in node properties
        return {"ui": {"text": [text_to_display], "last_input": [current_input]}, "result": (text_to_display,)}


NODE_CLASS_MAPPINGS = {
    "renderPrompt": RenderPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "renderPrompt": "Character Prompt Builder - Render Prompt",
}