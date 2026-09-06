class AddPrefixNode:
    """Add a prefix to a prompt string."""

    CATEGORY = "AzureAbyss/Prompt"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "add_prefix"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "prefix": ("STRING", {"default": "高品質、"}),
            }
        }

    def add_prefix(self, text, prefix):
        return (prefix + text,)
