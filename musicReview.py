import pandas as pd

def song_rating(song):
    table = pd.read_csv("data/tableMusic.csv")
    # Localizar a música com base no título
    song_selected = table.loc[table['title'].str.lower() == song.lower()]
    print("song selected", song_selected)
    # Verificar se a música foi encontrada
    if not song_selected.empty:
        # Exibir informações sobre a música
        print(" Song information:")
        print(" ", song_selected[['title', 'style', 'year', 'artist']])

        # Solicitar ao usuário uma avaliação (limitada a números inteiros de 0 a 5)
        try:
            user_rating = int(input(" Enter your rating for this song (0 to 5)=> "))
            if 0 <= user_rating <= 5:
                # Atualizar a avaliação na tabela de músicas
                table.loc[song_selected.index, 'rating_user'] = user_rating
                # Salvar as alterações de volta no arquivo CSV
                table.to_csv('data/tableMusic.csv', index=False)
            else:
                print(" Please enter a number from 0 to 5.")
        except ValueError:
            print("\033[1m WARNING: \033[0;0mPlease enter an integer from 0 to 5.")

        print(f" Song {song} reviewed successfully!")
