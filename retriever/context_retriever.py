def setup_retriever(vector_store, top_k = 3):

    retriever = vector_store.as_retriever(search_kwargs = {'k': top_k})

    return retriever