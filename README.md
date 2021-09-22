# DAG Data Pipelines med d6tflow

## Bygg og kjør dockerfila

### Bygg

```bash
docker build -t my-scipy-notebook ./

```

### Kjør

```bash
docker run --rm -p 9999:9999 \
  --env-file .env \
  -v "$PWD":/home/jovyan/work my-scipy-notebook
```

### Gå til

[localhost:9999](localhost:9999)
