navbars = [
    "edc_navbar.nav_administration",
    "edc_navbar.nav_ae_section",
    "edc_navbar.nav_data_manager_section",
    "edc_navbar.nav_home",
    "edc_navbar.nav_lab_aliquot",
    "edc_navbar.nav_lab_manifest",
    "edc_navbar.nav_lab_pack",
    "edc_navbar.nav_lab_process",
    "edc_navbar.nav_lab_receive",
    "edc_navbar.nav_lab_requisition",
    "edc_navbar.nav_lab_section",
    "edc_navbar.nav_logout",
    "edc_navbar.nav_pharmacy_section",
    "edc_navbar.nav_public",
    "edc_navbar.nav_screening_section",
    "edc_navbar.nav_subject_section",
    "edc_navbar.nav_tmg_section",
]

navbar_tuples = []
for codename in navbars:
    navbar_tuples.append((codename, f"Can access {codename.split('.')[1]}"))
