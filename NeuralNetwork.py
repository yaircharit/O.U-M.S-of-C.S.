import h5py

db = h5py.File('Data.h5')
im_names = list(db['data'].keys())
print(im_names)

im = im_names[0]
img = db['data'][im][:]
font = db['data'][im].attrs['font']
txt = db['data'][im].attrs['txt']
charBB = db['data'][im].attrs['charBB']
wordBB = db['data'][im].attrs['wordBB']
print(db['data'][im])