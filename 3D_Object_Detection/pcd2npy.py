import os
from pypcd import pypcd
import numpy as np
from glob import glob
import argparse
from tqdm import tqdm



def main():
    parser = argparse.ArgumentParser(description="Convert .pcd to .npy")
    parser.add_argument(
        "--pcd_path", "-p",
        help=".pcd file path.",
        type=str
    )
    parser.add_argument(
        "--npy_path", "-n",
        help=".npy file path.",
        type=str
    )
    parser.add_argument(
        "--walk", "-w",
        help="Walk through the directory",
        type=bool,
        default=False
    )
    args = parser.parse_args()
    
    def save_npy(lidar):
        pc = pypcd.PointCloud.from_path(lidar)
        points = np.vstack((pc.pc_data['x'], pc.pc_data['y'], pc.pc_data['z'])).transpose()
        np.save(args.npy_path+"/"+lidar.split("/")[-1][:-4]+".npy", points)
    
    if not args.walk:
        pcd_files = sorted(glob(os.path.join(args.pcd_path, "*.pcd")))

        for lidar in tqdm(pcd_files):
            save_npy(lidar)
    if args.walk:
        pcd_files = []
        for (path, dir, files) in os.walk(args.pcd_path):
            if '30_전방' in path:
                for filename in files:
                    ext = os.path.splitext(filename)[-1]
                    if ext == '.pcd':
                        pcd_files.append("%s/%s" % (path, filename))
                        
        for lidar in tqdm(pcd_files):
            save_npy(lidar)
    
    
if __name__ == "__main__":
    main()