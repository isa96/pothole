git clone https://github.com/AlexeyAB/darknet

cd darknet/
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/LIBSO=0/LIBSO=1/' Makefile

make

cd data/
find -maxdepth 1 -type f -exec rm -rf {} \;
cd ..

rm -rf cfg/
mkdir cfg

cd ..

mv ./yolov4-custom.cfg darknet/cfg

mv ./obj.names darknet/data
mv ./obj.data  darknet/data

mkdir uploads

mkdir model
gdown --id 1QSdGg7RM0rMrp2zWdjMoAQ9r0Vs71oVL
mv ./yolov4-custom_best.weights model