import openai

openai.api_key = 'YOUR_API_KEY'

resume_content = """
[Insert Resume Content Here]
"""

prompt = f"""
I will provide you with a resume which you have to analyse and extract the information from. Please parse the content of the resume into the following JSON format:

{{
  "name": "",
  "contact_information": {{
    "email": "",
    "phone": "",
    "address": ""
  }},
  "summary": "",
  "experience": [
    {{
      "job_title": "",
      "company": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "responsibilities": ""
    }}
  ],
  "education": [
    {{
      "degree": "",
      "university": "",
      "location": "",
      "graduation_date": ""
    }}
  ],
  "skills": []
}}

Points to remember:
1. You can leave the places blank if the content is missing. Fill the null values according to the data type of the key.
2. Do not make any major assumptions on your end and strictly parse the resume content on the basis of the given content.

Here is the resume:
{resume_content}
"""

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1500
)

print(response.choices[0].text.strip())
