# r3api

## ZingMp3

 - search
```python
ZingMp3.search("sontungmtp")
ZingMp3.search("sontungmtp", "song")
ZingMp3.search("sontungmtp", "playlist")
ZingMp3.search("sontungmtp", "artist")
ZingMp3.search("sontungmtp", "video")
```
 - song
```python
ZingMp3.getInfoMusic("ZW9CEAF8")
ZingMp3.getStreaming("ZW9CEAF8")
ZingMp3.getFullInfo("ZW9CEAF8")
ZingMp3.getRecommendSongs("ZW9CEAF8")
```
 - artist
```python
ZingMp3.getDetailArtist("AMEE")
```

 - playlist
```python
ZingMp3.getDetailPlaylist("ZOEE000F")
```

 - chart
```python
ZingMp3.getHome()
ZingMp3.getChartHome()
ZingMp3.getWeekChart("IWZ9Z08I")
ZingMp3.getNewReleaseChart()
ZingMp3.getTop100()
```