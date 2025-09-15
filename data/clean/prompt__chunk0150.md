# Prompt

Classify movie reviews as positive, neutral or negative. Return valid JSON:

Review: "Her" is a disturbing study revealing the direction humanity is headed if AI is allowed to keep evolving, unchecked. It's so disturbing I couldn't watch it.

Schema: ``` MOVIE: { "sentiment": String "POSITIVE" | "NEGATIVE" | "NEUTRAL", "name": String } MOVIE REVIEWS: { "movie_reviews": [MOVIE] } ``` JSON Response: