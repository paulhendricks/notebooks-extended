.PHONY: all build run

DOCKER_ID=$(shell docker ps --no-trunc -q)

#docker inspect --format="{{.Id}}"

all: run

build: 
	docker build -t notebooks-extended .

run: build
	docker run \
	  --runtime "nvidia" \
	  -it --rm \
	  -p 8786:8786 -p 8787:8787 -p 8888:8888 \
	  -v /datasets/rapids:/datasets/rapids \
	  -v /datasets/rapids_data:/datasets/rapids_data \
	  notebooks-extended

login:
	docker exec -it $(DOCKER_ID) bash

clean:
	rm -rf tutorials

copy: clean
	docker cp $(DOCKER_ID):/rapids/notebooks/extended/tutorials .

convert:
	jupyter nbconvert --to script foo.ipynb 

launch:
	source activate rapids && sh /rapids/notebooks/utils/start-jupyter.sh


