import pandas as pd

def song_rating():
    # Carregar o DataFrame da tabela de músicas
    tableMusic_df = pd.read_csv('data/tableMusic.csv', names=['id_music', 'style', 'type', 'title', 'songwritter', 'year', 'artist', 'rating_global', 'rating_user', 'duration'])

    while True:
        # Solicitar ao usuário o título  da música
        song_input = input("Please enter the title of the song you want to rate (or EXIT): ")

        # Verificar se o usuário deseja sair
        if song_input.lower() == 'exit':
            print("Exiting the application...")
            break

        # Localizar a música com base no título
        song_selected = tableMusic_df.loc[tableMusic_df['title'] == song_input]

        # Verificar se a música foi encontrada
        if not song_selected.empty:
            # Exibir informações sobre a música
            print("Song information:")
            print(song_selected[['title', 'style', 'year', 'artist']])

            # Solicitar ao usuário uma avaliação (limitada a números inteiros de 0 a 5)
            while True:
                try:
                    user_rating = int(input("Enter your rating for this song (0 to 5): "))
                    if 0 <= user_rating <= 5:
                        break  # Sai do loop se a avaliação estiver no intervalo correto
                    else:
                        print("Please enter a number from 0 to 5.")
                except ValueError:
                    print("Please enter an integer from 0 to 5.")

            # Atualizar a avaliação na tabela de músicas
            tableMusic_df.loc[song_selected.index, 'rating_user'] = user_rating

            # Salvar as alterações de volta no arquivo CSV
            tableMusic_df.to_csv('tableMusic.csv', index=False)

            print(f"Song {song_input} review has been updated successfully!")
            break  # Sair do loop depois de processar com sucesso
        else:
            print(f"Song '{song_input}' not found. Please try again.")

# Chamar a função para permitir que o usuário avalie uma música
