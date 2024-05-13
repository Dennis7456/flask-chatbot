example = [
       {
        "question": "hi",
        "query": "MATCH (:Bot)-[:ASKS]->(:Question {text: 'hi'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question": "hey",
        "query" : "MATCH (:Bot)-[:ASKS]->(:Question {text: 'hey'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"

    },
    {
        "question": "What's your name",
        "query" : "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'What's your name?'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question": "Can you tell me more about Lake Naivasha?",
        "query": "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'Can you tell me more about Lake Naivasha?'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question": "Can you tell me a joke?",
        "query": "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'Can you tell me a joke?'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question":"What's the best movie you've ever seen?",
        "query": "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'What's the best movie you've ever seen?'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question": "How do I change a flat tire?",
        "query": "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'How do I change a flat tire?'})-[:HAS_ANSWER]->(answer:Answer) RETURN answer.text AS response"
    },
    {
        "question": "How do I start a business?",
        "query": "MATCH (:Bot {name: 'Tom'})-[:ASKS]->(:Question {text: 'How do I start a business?'})-[:HAS_ANSWER]->(answer:Answer)RETURN answer.text AS response"
    }
]