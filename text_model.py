import cohere
from cohere.classify import Example

co = cohere.Client('DLHq9Go9DHorXORElej8QEbINQZYq3NrM0G3RsGo')

inputs = ["beach ball"]

response = co.classify(
    model='large',
    inputs=inputs,
    examples=examples)

# print("Formatted version: {}".format(response.classifications)[0])
# print("Formatted version: {}".response.classifications[0])
print(response.classifications[0].prediction)
print(response.classifications[0].confidence)
print(response.classifications[0].labels)
