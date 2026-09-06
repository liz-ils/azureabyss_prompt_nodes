"""AzureAbyss Prompt Nodes for ComfyUI."""

from .prompt_node import AddPrefixNode, PromptFormatter

NODE_CLASS_MAPPINGS = {
    "AzureAbyss.AddPrefix": AddPrefixNode,
    "AzureAbyss.PromptFormatter": PromptFormatter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AzureAbyss.AddPrefix": "Add Prompt Prefix",
    "AzureAbyss.PromptFormatter": "Prompt Formatter",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
