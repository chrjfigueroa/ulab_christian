# File photon_energies.py

import numpy as np

c = 2.99792458e17 # Speed of light in nm/s
h = 4.1357e-15 # Planck's constant in eV*seconds
H_IONIZATION_ENERGY = 13.6 # In eVs
H_ALPHA_ENERGY = 1.89 # In eVs
H_BETA_ENERGY = 2.55 # In eVs
H_GAMMA_ENERGY = 2.86 # In eVs
H_DELTA_ENERGY = 3.02 # In eVs

def energy_of_photons(photon_wavelengths):
    """
    Calculates the energies in eV of photons in photon packets given their wavelengths.
    E = h*c/λ

    Input:
    photon_wavelengths (numpy.ndarray): 2D list of photon wavelengths in each packet of photons.

    Output:
    energies (numpy.ndarray): 2D list of photon energies corresponding to each photon wavelength.
    """
    photon_wavelengths = photon_wavelengths.astype('float64')
    for packet in photon_wavelengths: 
        for i,wavelength in enumerate(packet):
            energy = (h*c)/wavelength
            packet[i] = np.format_float_scientific(energy, precision=5)  
    energies = photon_wavelengths 

    return energies
    
def wavelength_to_frequency(photon_wavelength):
    """
    This function converts the wavelengths of each photon in a photon packet into frequencies.
    f=c/λ
    
    Input:
    photon_wavelengths (numpy.ndarray): 2D list of photon wavelengths in each packet of photons.

    Output:
    frequencies (numpy.ndarray): 2D list of photon energies corresponding to each photon wavelength.
    """
    photon_wavelength = photon_wavelength.astype('float64')
    for packet in photon_wavelength: 
        for i,wavelength in enumerate(packet):
            frequency = c/wavelength
            packet[i] = np.format_float_scientific(frequency, precision=5)  
    frequencies = photon_wavelength

    return frequencies

def hydrogen_status(wavelengths):
    """
    Returns status of hydrogen visual absorption lines for each packet of photons.

    Input:
    wavelengths (numpy.ndarray): 2D list of photon wavelengths in each packet of photons.

    Output:
    hydrogen_status (list): list of status of hydrogen for each photon packet.
    """

    hydrogen_status = []

    # Turns wavelengths into energies
    photon_energies = energy_of_photons(wavelengths)
    
    for energies in photon_energies:
        IONIZE=0
        Hα = 0
        Hβ = 0
        Hγ = 0
        Hδ = 0
        NONE = 0
        for energy in energies:
            if energy >= H_IONIZATION_ENERGY:
                IONIZE += 1
            elif (H_ALPHA_ENERGY-0.02) < energy < (H_ALPHA_ENERGY+0.02):
                Hα += 1
            elif (H_BETA_ENERGY-0.02) < energy < (H_BETA_ENERGY+0.02):
                Hβ += 1
            elif (H_GAMMA_ENERGY-0.02) < energy < (H_GAMMA_ENERGY+0.02):
                Hγ += 1
            elif (H_DELTA_ENERGY-0.02) < energy < (H_DELTA_ENERGY+0.02):
                Hδ += 1
            else:
                NONE += 1
                
        status = str(IONIZE)+" ionized. " +str(Hα)+" alpha-lines produced. "+str(Hβ)+" beta-lines produced. "+str(Hγ)+" gamma-lines produced. "+str(Hδ)+" delta-lines produced. "+str(NONE)+" remaining photons."
        hydrogen_status.append([status])
    finished_status = np.array(hydrogen_status)
    return finished_status


            