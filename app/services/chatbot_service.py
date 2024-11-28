
def get_predefined_response(message: str) -> dict:
    predefined_responses = {
        "ver projetos": {
            "response": "Esses são alguns dos meus projetos mais recentes.",
            "options": ["Aplicativo de Receitas", "E-commerce de Granolas", "To-do List com Redux", "Ver Mais"]
        },
        "ver experiência": {
            "response": "Tenho 3 anos de experiência em desenvolvimento front-end, com foco em tecnologias como React e Next.js.",
            "options": ["Ver Projetos Detalhados", "Ver Habilidades"]
        },
        "ver habilidades técnicas": {
            "response": "Aqui estão minhas principais habilidades técnicas.",
            "options": ["JavaScript e React", "Next.js e TypeScript", "UI/UX e Design Responsivo", "Ver Todas"]
        },
    }

    message_lower = message.lower()

    for intent, response in predefined_responses.items():
        if intent in message_lower:
            return response

    return None
