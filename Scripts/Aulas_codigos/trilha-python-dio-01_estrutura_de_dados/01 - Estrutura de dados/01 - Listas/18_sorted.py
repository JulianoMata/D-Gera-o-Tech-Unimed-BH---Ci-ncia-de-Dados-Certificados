linguagens = ["python", "js", "c", "java", "csharp"]
# função similar ao metodo sort
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print(sorted(linguagens))
