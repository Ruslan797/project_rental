from functools import lru_cache

from sentence_transformers import SentenceTransformer, util

from rental_connects.models.booking import Advertisement


@lru_cache(maxsize=1)
def get_recommendation_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def build_advertisement_text(advertisement: Advertisement) -> str:
    address = advertisement.address
    parts = [
        advertisement.title or "",
        advertisement.description or "",
        advertisement.type_of_property or "",
        advertisement.infrastructure or "",
        address.country if address else "",
        address.city if address else "",
        address.region if address else "",
        address.street if address else "",
        f"price {advertisement.price}" if advertisement.price is not None else "",
        f"area {advertisement.area}" if advertisement.area is not None else "",
        f"rooms {advertisement.number_of_rooms}" if advertisement.number_of_rooms is not None else "",
    ]
    return " ".join(str(part).strip() for part in parts if part)


def get_similar_advertisements(advertisement_id: int, top_k: int = 5):
    target = (
        Advertisement.objects
        .select_related("address")
        .get(pk=advertisement_id)
    )

    candidates = list(
        Advertisement.objects
        .select_related("address")
        .exclude(pk=target.pk)
        .filter(status="active")
    )

    if not candidates:
        return []

    model = get_recommendation_model()

    target_text = build_advertisement_text(target)
    candidate_texts = [build_advertisement_text(ad) for ad in candidates]

    target_embedding = model.encode(target_text, convert_to_tensor=True)
    candidate_embeddings = model.encode(candidate_texts, convert_to_tensor=True)

    similarities = util.cos_sim(target_embedding, candidate_embeddings)[0]

    scored = []
    for ad, score in zip(candidates, similarities):
        scored.append({
            "advertisement": ad,
            "score": round(float(score), 4)
        })

    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]