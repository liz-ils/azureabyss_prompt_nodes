"""AzureAbyss Prompt Nodes for ComfyUI."""

from .prompt_node import AddPrefixNode

NODE_CLASS_MAPPINGS = {
    "AzureAbyss.AddPrefix": AddPrefixNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AzureAbyss.AddPrefix": "Add Prompt Prefix",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
