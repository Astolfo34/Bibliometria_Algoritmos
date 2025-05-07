def normalize_entry(raw_entry, source):
    FIELD_MAPPING = {
        "scopus": {
            "title": ["dc:title"],
            "authors": ["dc:creator"],
            "abstract": ["dc:description"],
            "doi": ["prism:doi"]
        },
        "web_of_science": {
            "title": ["TI"],
            "authors": ["AU"],
            "abstract": ["AB"]
        }
    }

    normalized = {}
    for target_field, source_fields in FIELD_MAPPING[source].items():
        for field in source_fields:
            if field in raw_entry:
                normalized[target_field] = raw_entry[field]
                break
    return normalized