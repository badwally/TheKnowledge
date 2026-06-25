import numpy as np
from gateway.embedding_index import Encoder
from gateway.retrieval_encoder import StubRetrievalEncoder


def test_stub_encoder_satisfies_protocol_and_is_deterministic():
    enc = StubRetrievalEncoder(dim=256)
    assert isinstance(enc, Encoder)            # runtime_checkable Protocol
    assert enc.dim == 256 and enc.model_version
    v1 = enc.embed(["hello world"])[0]
    v2 = enc.embed(["hello world"])[0]
    assert v1 == v2                            # deterministic
    assert len(v1) == 256
    assert abs(float(np.linalg.norm(v1)) - 1.0) < 1e-5   # L2-normalized


def test_stub_encoder_paraphrase_closer_than_unrelated():
    enc = StubRetrievalEncoder(dim=256)
    import numpy as np
    a, b, c = (np.asarray(enc.embed([t])[0]) for t in
               ["central bank selling bonds", "central bank sells bonds", "banana bread recipe"])
    assert float(a @ b) > float(a @ c)         # paraphrase nearer than unrelated
