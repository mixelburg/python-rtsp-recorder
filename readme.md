

## run rtsp server

```bash
docker run --rm -it -v $PWD/rtsp-simple-server.yml:/rtsp-simple-server.yml -p 8554:8554 aler9/rtsp-simple-server
```


## run ffmpeg

```bash
ffmpeg -re -stream_loop -1 -i .\center.mp4 -f rtsp -rtsp_transport tcp rtsp://127.0.0.1:8554/axis-media/media.amp
```
