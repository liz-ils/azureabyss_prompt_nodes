class AddPrefixNode:
    """Add a prefix to a prompt string."""

    CATEGORY = "AzureAbyss/Prompt"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "add_prefix"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "prefix": ("STRING", {"default": "高品質、"}),
                "mode": (["prefix", "suffix", "both"],),
            }
        }

    def add_prefix(self, text, prefix, mode):
        if mode == "suffix":
            return (text + prefix,)
        if mode == "both":
            return (prefix + text + prefix,)
        return (prefix + text,)
