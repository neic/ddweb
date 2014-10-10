SELECT title, FROM_UNIXTIME(`timestamp`,'%d/%m/%Y %H:%i:%S'),body, `field_author_value`, `field_img1_value`, `field_img2_value`, `field_img3_value`, `field_img4_value`, `field_img5_value`, `field_img6_value`, `field_img7_value`, `field_img8_value`, `field_img9_value`, `field_img10_value` FROM `cbhanse_content_type_news` INNER JOIN cbhanse_node_revisions ON cbhanse_node_revisions.vid=`cbhanse_content_type_news`.vid


SELECT title, FROM_UNIXTIME(`timestamp`,'%d/%m/%Y %H:%i:%S'),body, `field_author_value` FROM `cbhanse_content_type_news` INNER JOIN cbhanse_node_revisions ON cbhanse_node_revisions.vid=`cbhanse_content_type_news`.vid
