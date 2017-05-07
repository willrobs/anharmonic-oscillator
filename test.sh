niter=10000
points=400
a=0.05
step=0.5
ttime=2000
mass=0.5
mu2=-2
anharm=0.2
corrdist=500
bootsamp=75
eecorrdist=15
d_volume=0.01
data_sets=200
mprime=1.8
muprime=10.2
python data.py $niter $points $a $step $ttime $mass $mu2 $anharm

python bin.py $niter $points $a $corrdist $mass $mu2 $anharm

python gse.py $niter $points $a $bootsamp $mass $mu2 $anharm

python fee.py $niter $points $a $eecorrdist $bootsamp $mass $mu2 $anharm

python probd.py $niter $points $a $d_volume $data_sets $mass $mu2 $anharm

python reweight.py $niter $points $a $eecorrdist $bootsamp $mprime $muprime $mass $mu2 $anharm