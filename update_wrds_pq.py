from db2pq import wrds_update_pq

# CRSP
wrds_update_pq('stocknames', 'crsp')
wrds_update_pq('dsedist', 'crsp')
wrds_update_pq('msi', 'crsp')
wrds_update_pq('msf', 'crsp')
