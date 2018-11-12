from .group_names import (
    ACCOUNT_MANAGER, ADMINISTRATION, PII_VIEW,
    EVERYONE, AUDITOR, CLINIC, LAB, PHARMACY, PII,
    EXPORT, DATA_MANAGER)

DEFAULT_CODENAMES = {
    ACCOUNT_MANAGER: [
        'add_group',
        'add_notification',
        'add_permission',
        'add_user',
        'add_userprofile',
        'change_group',
        'change_notification',
        'change_permission',
        'change_user',
        'change_userprofile',
        'delete_group',
        'delete_notification',
        'delete_permission',
        'delete_user',
        'delete_userprofile',
        'view_group',
        'view_notification',
        'view_permission',
        'view_user',
        'view_userprofile'],
    ADMINISTRATION: ['nav_administration'],
    AUDITOR: [
        'nav_lab_requisition',
        'nav_lab_section',
        'view_actionitem',
        'view_actionitemupdate',
        'view_actiontype',
        'view_aliquot',
        'view_appointment',
        'view_box',
        'view_boxitem',
        'view_boxtype',
        'view_consignee',
        'view_historicalactionitem',
        'view_historicalactionitemupdate',
        'view_historicalaliquot',
        'view_historicalappointment',
        'view_historicalbox',
        'view_historicalboxitem',
        'view_historicalconsignee',
        'view_historicalmanifest',
        'view_historicalorder',
        'view_historicalresult',
        'view_historicalresultitem',
        'view_historicalshipper',
        'view_historicalsubjectoffstudy',
        'view_lab_requisition_listboard',
        'view_manifest',
        'view_manifestitem',
        'view_order',
        'view_panel',
        'view_reference',
        'view_result',
        'view_resultitem',
        'view_shipper',
        'view_subjectoffstudy'],
    CLINIC: [
        'add_actionitem',
        'add_actionitemupdate',
        'add_actiontype',
        'add_appointment',
        'add_reference',
        'add_subjectoffstudy',
        'change_actionitem',
        'change_actionitemupdate',
        'change_actiontype',
        'change_appointment',
        'change_reference',
        'change_subjectoffstudy',
        'delete_actionitem',
        'delete_actionitemupdate',
        'delete_actiontype',
        'delete_reference',
        'delete_subjectoffstudy',
        'nav_lab_requisition',
        'nav_lab_section',
        'view_actionitem',
        'view_actionitemupdate',
        'view_actiontype',
        'view_appointment',
        'view_historicalactionitem',
        'view_historicalactionitemupdate',
        'view_historicalappointment',
        'view_historicalsubjectoffstudy',
        'view_lab_requisition_listboard',
        'view_reference',
        'view_subjectoffstudy',
    ],
    DATA_MANAGER: [
        'add_crfmetadata',
        'add_requisitionmetadata',
        'change_crfmetadata',
        'change_requisitionmetadata',
        'delete_crfmetadata',
        'delete_requisitionmetadata',
        'view_crfmetadata',
        'view_requisitionmetadata'],
    EVERYONE: [
        'view_group',
        'view_logentry',
        'view_permission',
        'view_site',
        'view_user',
        'view_userprofile',
    ],
    EXPORT: [
        'add_datarequest',
        'add_datarequesthistory',
        'add_exportreceipt',
        'add_filehistory',
        'add_objecthistory',
        'add_plan',
        'add_uploadexportreceiptfile',
        'change_datarequest',
        'change_datarequesthistory',
        'change_exportreceipt',
        'change_filehistory',
        'change_objecthistory',
        'change_plan',
        'change_uploadexportreceiptfile',
        'delete_datarequest',
        'delete_datarequesthistory',
        'delete_exportreceipt',
        'delete_filehistory',
        'delete_objecthistory',
        'delete_plan',
        'delete_uploadexportreceiptfile',
        'view_datarequest',
        'view_datarequesthistory',
        'view_exportreceipt',
        'view_filehistory',
        'view_historicaldatarequest',
        'view_historicalexportreceipt',
        'view_historicalfilehistory',
        'view_historicalobjecthistory',
        'view_historicalplan',
        'view_objecthistory',
        'view_plan',
        'view_uploadexportreceiptfile',
    ],
    LAB: [
        'add_aliquot',
        'add_box',
        'add_boxitem',
        'add_boxtype',
        'add_consignee',
        'add_manifest',
        'add_manifestitem',
        'add_order',
        'add_panel',
        'add_result',
        'add_resultitem',
        'add_shipper',
        'change_aliquot',
        'change_box',
        'change_boxitem',
        'change_boxtype',
        'change_consignee',
        'change_manifest',
        'change_manifestitem',
        'change_order',
        'change_panel',
        'change_result',
        'change_resultitem',
        'change_shipper',
        'delete_aliquot',
        'delete_box',
        'delete_boxitem',
        'delete_boxtype',
        'delete_consignee',
        'delete_manifest',
        'delete_manifestitem',
        'delete_order',
        'delete_panel',
        'delete_result',
        'delete_resultitem',
        'delete_shipper',
        'nav_lab_aliquot',
        'nav_lab_manifest',
        'nav_lab_pack',
        'nav_lab_process',
        'nav_lab_receive',
        'nav_lab_requisition',
        'nav_lab_section',
        'view_aliquot',
        'view_box',
        'view_boxitem',
        'view_boxtype',
        'view_consignee',
        'view_historicalaliquot',
        'view_historicalbox',
        'view_historicalboxitem',
        'view_historicalconsignee',
        'view_historicalmanifest',
        'view_historicalorder',
        'view_historicalresult',
        'view_historicalresultitem',
        'view_historicalshipper',
        'view_lab_aliquot_listboard',
        'view_lab_box_listboard',
        'view_lab_manifest_listboard',
        'view_lab_pack_listboard',
        'view_lab_process_listboard',
        'view_lab_receive_listboard',
        'view_lab_requisition_listboard',
        'view_lab_result_listboard',
        'view_manifest',
        'view_manifestitem',
        'view_order',
        'view_panel',
        'view_result',
        'view_resultitem',
        'view_shipper'],
    PHARMACY: [
        'add_appointment',
        'add_dispenseditem',
        'add_dosageguideline',
        'add_medication',
        'add_prescription',
        'add_prescriptionitem',
        'change_appointment',
        'change_dispenseditem',
        'change_dosageguideline',
        'change_medication',
        'change_prescription',
        'change_prescriptionitem',
        'delete_appointment',
        'delete_dispenseditem',
        'delete_dosageguideline',
        'delete_medication',
        'delete_prescription',
        'delete_prescriptionitem',
        'nav_pharmacy_section',
        'view_appointment',
        'view_dispenseditem',
        'view_dosageguideline',
        'view_medication',
        'view_prescription',
        'view_prescriptionitem'],
    PII: ['add_subjectlocator',
          'change_subjectlocator',
          'delete_subjectlocator',
          'display_dob',
          'display_firstname',
          'display_identity',
          'display_initials',
          'display_lastname',
          'view_registeredsubject',
          'view_subjectlocator'],
    PII_VIEW: [
        'display_dob',
        'display_firstname',
        'display_identity',
        'display_initials',
        'display_lastname',
        'view_registeredsubject',
        'view_subjectlocator'],
}
