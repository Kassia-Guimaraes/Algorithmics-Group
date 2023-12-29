import pandas as pd

def song_rating(table):
    # Carregar o DataFrame da tabela de músicas
    while True:
        # Solicitar ao usuário o título  da música
        songs_list = sorted(list(table['title'].drop_duplicates()))
        print("\033[1m AVAILABLE SONGS \033[0;0m")
        for title in songs_list:
            print(" ", title)

        song_input = input(" What song do you want to rate (or 0 to exit)=> ").lower()

        # Verificar se o usuário deseja sair
        if song_input == '0':
            print("Exiting the application...")
            break

        # Localizar a música com base no título
        song_selected = table.loc[table['title'].str.lower() == song_input]
        print("song selected", song_selected)
        # Verificar se a música foi encontrada
        if not song_selected.empty:
            # Exibir informações sobre a música
            print(" Song information:")
            print(" ", song_selected[['title', 'style', 'year', 'artist']])

            # Solicitar ao usuário uma avaliação (limitada a números inteiros de 0 a 5)
            while True:
                try:
                    user_rating = int(input(" Enter your rating for this song (0 to 5)=> "))
                    if 0 <= user_rating <= 5:
                        break  # Sai do loop se a avaliação estiver no intervalo correto
                    else:
                        print(" Please enter a number from 0 to 5.")
                except ValueError:
                    print("\033[1m WARNING: \033[0;0mPlease enter an integer from 0 to 5.")

            # Atualizar a avaliação na tabela de músicas
            table.loc[song_selected.index, 'rating_user'] = user_rating

            # Salvar as alterações de volta no arquivo CSV
            table.to_csv('tableMusic.csv', index=False)

            print(f" Song {song_input} reviewed successfully!")
            break  # Sair do loop depois de processar com sucesso
        else:
            print(f"\033[1m WARNING: \033[0;0mSong '{song_input}' not found. Please try again.")
