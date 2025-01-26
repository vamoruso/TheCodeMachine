import re

import ollama

# Initialize the Ollama client
client = ollama.Client()

# Read the Java source file
with open('D:/TheCodeMachine/HelloWorld.java', 'r') as file:
    java_code = file.read()

language_extensions = {
    "Cobol":"cbl",
    "RPG iSeries RPG (Report Program Generator) on IBM iSeries (AS/400)":"RPG",
    "Python": "py",
    "Dart": "dart",
    "JavaScript": "js",
     "C": "c",
    "C++": "cpp",
    "C#": "cs",
    "Ruby": "rb",
    "Go": "go",
    "Swift": "swift",
    "Kotlin": "kt",
    "PHP": "php",
    "HTML": "html",
    "CSS": "css",
    "TypeScript": "ts",
    "R": "r",
    "Perl": "pl",
    "Scala": "scala",
    "Rust": "rs",
    "Objective-C": "m",
    "Visual Basic": "vb",
    "Pascal": "pas",
}

# Iterate over the dictionary
for language, extension in language_extensions.items():
    print(f"The file extension for {language} is .{extension}")


    # Define the prompt for the model
    prompt = f"Convert the following Java code to {language}:\n\n{java_code}"

    # Call the Qwen2.5-Coder:32B model
    response = client.generate(model="qwen2.5-coder:32b", prompt=prompt)

    # Convert the response to a string if it's not already
    response_str = str(response)
    # Use regular expressions to find code blocks
    code_blocks = re.findall(r'```(.*?)```', response_str, re.DOTALL)

    # Join the extracted code blocks
    extracted_code = "\n\n".join(code_blocks).replace("\\n", "\n")

    rows=extracted_code.split("\n")
    rows=rows[1:]
    extracted_code="\n\n".join(rows)

    print(extracted_code)

    # Write the Dart code to a file
    with open(f'D:/TheCodeMachine/HelloWorld.{extension}', 'w') as file:
        file.write(extracted_code)

print("Conversion completed!")
