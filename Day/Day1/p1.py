#Variables
temperature = 0.7 #float by default
max_tokens = 1024 #int 
content_box = None #None
#Type hints
temperature : float = 0.7 #float by default
max_tokens : int = 1024 #int 
content_box : str|None = None #None
model_name: str = "gemini-2.0-flash"

print(type(model_name))

#Strings:immutable | string formating
#Old_ver
name="LLM"
score = 97.3
print("Hello %s"%name)
print("Score %.1f"%score)

# f - string (py 3.6+)
print(f"Hello {name}")
print(f"Score: {score}")

#Expressions inside the f-strings
word_limit = 200
print(f"{'Over'if word_limit > 150 else 'under'} limit")
data={"topic":"rag"}
print(f"Topic:{data['topic']}")

#Format specifiers
pi = 3.14159
print(f'{pi:.2f}')

#Debugging =
temp =0.5
print(f'{temp=}')
#multi- line - f - string format
user_input="What is langchain"
context_text="Langchain is a framework foor building application with us"
system_prompt=f"""you are a helpful assistant.
context provided: {context_text}
student question: {user_input}
Instructions:
-answer based only on the context above 
-if the answer is not in the context, say "I don't know"
-keep your answers under 3 sentences
""".strip() # remove leading and trailing whitespace
print(system_prompt)

#Lists: ordered,mutable,heterogenous sequences 
#In Gen AI: Chat history, chunks of retreived documents
#token sequences
chat_history: list[dict] = [ {'role':'user','content':"What is an LLM"},{'role':'assistant',"content":"A LLM is a neural network trained on vast amount of text. "},
]
# Acess
first_msg = chat_history[0]
print(first_msg) 
print(chat_history[-1]['content']) # last element in the list

#Modify
chat_history.append({"role":"user","content":"what is RAG?"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#Iterate
for msg in chat_history:
    print(f'{msg['role'].upper()}:{msg['content']}')

#List of document chunks
chunks:list[str]=["RAG stands for Retreival Augmented Generation","It combines a retreiver with a generator"]
#Filter chunks based on length
valid_chunks = [c for c in chunks if len(c.split())>=6]
print(valid_chunks)













