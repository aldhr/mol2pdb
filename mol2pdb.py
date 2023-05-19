## this vversion of the code is to be used as command-line tool
import os
import argparse
import pymol
from pymol import cmd

def convert_mol2_to_pdb(mol2_directory, output_directory):
    # Initialize PyMOL
    pymol.finish_launching(['pymol', '-cq'])

    for file in os.listdir(mol2_directory):
        if file.endswith('.mol2'):
            cmd.set('pdb_use_ter_records', 1)  # Use TER records for chain breaks
            cmd.load(os.path.join(mol2_directory, file), 'mol2_object')
            cmd.h_add('mol2_object')  # Add hydrogen atoms
            cmd.sort()  # Sort atoms
            pdb_file = os.path.splitext(file)[0] + '.pdb'
            cmd.save(os.path.join(output_directory, pdb_file), 'mol2_object')
            print(f"Converted {file} to {pdb_file}")

    # Quit PyMOL
    cmd.quit()

if _name_ == '_main_':
    parser = argparse.ArgumentParser(description='Convert mol2 files to PDB format using PyMOL.')
    parser.add_argument('mol2_directory', type=str, help='Directory containing mol2 files')
    parser.add_argument('--output_directory', type=str, default='pdbs', help='Output directory for PDB files')

    args = parser.parse_args()

    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    convert_mol2_to_pdb(args.mol2_directory, args.output_directory)

