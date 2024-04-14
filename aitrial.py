from characterai import pycai

def main():
    client = pycai.Client('39cf52482c896ef0c48e7be264537d9ff828c10d')

    char = client.create_char('Ava', "Hi I'm Ava",description="Technical Writer who enjoys Basketball. They value self-reliance and sociability")

    char_id = char.external_id

    me = client.get_me()

    with client.connect() as chat:
        new, answer = chat.new_chat(
            char_id, me.id
        )

        print(f'{answer.name}: {answer.text}')
        
        while True:
            text = input('YOU: ')

            message = chat.send_message(
                char_id, new.chat_id, text
            )

            print(f'{message.name}: {message.text}')

main()


# 39cf52482c896ef0c48e7be264537d9ff828c10d
# 'cfklHxgS3BB_81ZwOslozE96vXOt_r9rrqa_hianyDY'