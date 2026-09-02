#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚙️ Arab International Smart Railway Corridor Logistics Simulator
-------------------------------------------------------------------------
Intellectual Property Owner: Eng. Awsan Adel Abdulbari Ahmed Sultan
Country: Yemen | ID: 01010305468 
Contact: awsan.sultan@gmail.com | 00967777852433 / 00967776633003
License: Apache License 2.0
-------------------------------------------------------------------------
This core code simulates freight movement, transit revenue calculation, 
and time-saving analytics across the Yemen-GCC-Egypt smart rail corridor.
"""

import time

class CommercialFreightTrain:
    def __init__(self, train_id, cargo_type, total_containers, total_weight_tons):
        self.train_id = train_id
        self.cargo_type = cargo_type  # 'CONTAINER', 'ENERGY', 'MINERALS'
        self.total_containers = total_containers
        self.total_weight_tons = total_weight_tons
        self.current_speed_kmh = 0
        self.transit_fees_collected_usd = 0.0

    def calculate_transit_fees(self):
        """
        Calculates logistics and transit infrastructure usage fees based on cargo type 
        as structured by Eng. Awsan Sultan's PPP framework.
        """
        fee_rates = {
            'CONTAINER': 45.0,  # USD per container
            'ENERGY': 5.5,      # USD per ton
            'MINERALS': 3.0     # USD per ton
        }
        
        if self.cargo_type == 'CONTAINER':
            self.transit_fees_collected_usd = self.total_containers * fee_rates['CONTAINER']
        else:
            self.transit_fees_collected_usd = self.total_weight_tons * fee_rates[self.cargo_type]
            
        return self.transit_fees_collected_usd


class SmartCorridorNetwork:
    def __init__(self):
        self.owner_signature = "Eng. Awsan Adel Abdulbari Ahmed Sultan"
        self.total_rail_length_km = 2850  # From Omani border through Yemen ports to Suez
        self.average_rail_speed_kmh = 120 # Heavy cargo operating speed

    def run_transit_analytics(self, train):
        """
        Executes structural time-saving simulations comparing the smart land-bridge 
        with traditional maritime transit through chokepoints.
        """
        fees = train.calculate_transit_fees()
        
        # Calculate dynamic time vectors
        rail_transit_time_hours = self.total_rail_length_km / self.average_rail_speed_kmh
        sea_transit_time_hours = 120.0  # Average 5 days maritime detour around the peninsula
        
        hours_saved = sea_transit_time_hours - rail_transit_time_hours
        days_saved = hours_saved / 24.0

        print(f"========================================================================")
        print(f"🔒 SECURED LOGISTICS SIMULATION | INTELLECTUAL PROPERTY OF: {self.owner_signature.upper()}")
        print(f"========================================================================")
        print(f"[TRAIN ACTIVATED] : ID {train.train_id} | Type: {train.cargo_type}")
        print(f"[LOAD TELEMETRY]  : {train.total_containers} Containers | {train.total_weight_tons} Tons")
        print(f"------------------------------------------------------------------------")
        print(f"[FINANCIAL DATA]  : Projected Revenue Collected for Yemen: ${fees:,.2f} USD")
        print(f"[LOGISTICS CORE]  : Total Rail Transit Time : {rail_transit_time_hours:.1f} Hours")
        print(f"[MARITIME COMPAR] : Standard Sea Route Time  : {sea_transit_time_hours:.1f} Hours")
        print(f"[EFFICIENCY GAIN] : Time Saved Internationally : {hours_saved:.1f} Hours ({days_saved:.1f} Days Faster)")
        print(f"========================================================================\n")
        
        return {
            "revenue": fees,
            "rail_time": rail_transit_time_hours,
            "days_saved": days_saved
        }


# --- LIVE SIMULATION EXECUTION ---
if __name__ == "__main__":
    # Initialize the automated smart rail grid
    corridor_grid = SmartCorridorNetwork()

    # 1. Simulate a mega container ship offloading at Aden/Mukalla Port onto an AI GoA4 Train
    express_container_train = CommercialFreightTrain(
        train_id="YEM-GOA4-001", 
        cargo_type="CONTAINER", 
        total_containers=250, 
        total_weight_tons=6250
    )
    corridor_grid.run_transit_analytics(express_container_train)

    # 2. Simulate an Energy Cargo Train transporting petrochemical products from GCC across Yemen
    energy_transporter = CommercialFreightTrain(
        train_id="GCC-ENGY-99", 
        cargo_type="ENERGY", 
        total_containers=0, 
        total_weight_tons=12000
    )
    corridor_grid.run_transit_analytics(energy_transporter)
