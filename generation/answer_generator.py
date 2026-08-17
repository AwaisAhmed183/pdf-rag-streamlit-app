from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama


def generate_answer(retriever, query, model_name = 'qwen2.5:0.5b',
                        temperature = 0.1, max_tokens = 512):

    """Generate Answer using a local llm through ollama"""

    llm = Ollama(
        model = model_name,
        temperature = temperature,
        num_predict = max_tokens
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = 'stuff',
        retriever = retriever,
    )

    response = qa_chain.invoke({'query':query})

    return response['result']

