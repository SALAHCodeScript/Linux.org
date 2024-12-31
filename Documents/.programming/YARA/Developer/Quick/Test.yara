rule ExampleRule
{
    meta:
        author = "Your Name"
        description = "Detects example malware"
        date = "2024-12-04"
    strings:
        $text_string = "malware"          // A text string
        $hex_pattern = {6D 61 6C 77 61 72 65} // Hexadecimal pattern
        $regex = /mal.*re/               // Regular expression
    condition:
        $text_string or $hex_pattern or $regex
}
