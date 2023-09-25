def solution(genres, plays):
    answer = []
    
    # 장르별 많이 재생된 여부 파악을 위한 딕셔너리 생성
    # 장르 : [재생수, 곡번호]
    genres_dict = {idx: [genre, play] for idx, (genre, play) in enumerate(zip(genres, plays))}
    
    top_genres = {}
    for genre, play in genres_dict.values():
        if genre in top_genres :
            top_genres[genre] += play
        else :
            top_genres[genre] = play
    top_genres = sorted(top_genres.items(), key=lambda x: x[1], reverse = True)

    genres_dict = dict(sorted(genres_dict.items(), key = lambda item: item[1][1], reverse = True))
    
    for i in top_genres:
        # 장르별 노래 개수가 2개임을 체크하는 용도
        songs = 0
        for key, (genre, play) in genres_dict.items():
            if songs == 2 :
                break
            if i[0] == genre :
                answer.append(key)
                songs += 1
            
    return answer