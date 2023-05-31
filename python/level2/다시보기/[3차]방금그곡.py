# 참고함: https://beomcoder.tistory.com/71
from datetime import datetime, timedelta

def solution(m, musicinfos):
    answer = {'time': 0, 'name': '(None)'}
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for i in musicinfos:
        start, end, title, note = i.split(',')
        
        note = note.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        
        startTime = datetime.strptime(start, '%H:%M')
        endTime = datetime.strptime(end, '%H:%M')
        diff = endTime - startTime
        minutes = int(diff.total_seconds() / 60)

        note = (note * max(1, int(minutes / len(note)) + 1))[:minutes]
        
        if m in note and answer['time'] < minutes:
            answer = {'time': minutes, 'name': title}
        
    return answer['name']