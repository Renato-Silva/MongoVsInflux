#!/bin/bash
for i in {1472666050..1472667050}
do
    echo "Time $i"
    curl -i -XPOST "http://localhost:8086/write?db=weather&precision=s" --data-binary "temperature,location=1 value=90 $i"
done
