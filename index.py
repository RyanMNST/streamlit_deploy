import streamlit as st


def app():
    st.write("""
    # Finals System Web Application Version
    A [CS 321 | CS 322] Project - Recommender System
    """)
    st.write(
        'Alcid, Cuta, Javier, Malibiran, Melegrito, Ramos, Talipnao, Tomelden')

    st.header('Abstract')
    st.write('Contraceptive and maternal health within the Philippines has been a continuous endeavor for decades. With numerous programs and surveys conducted to understand patterns and behaviors from individuals residing in the country, the Philippines would still need to introduce new approaches to increase modern contraceptive use and improve sexual and reproductive health. This paper demonstrates the prospect that current methods have in making such tasks, modern techniques such as applying recommender systems.')
    st.write("The system acquired relevant data from the United States Agency for International Development’s (USAID) Demographic and Health Surveys (DHS) program. Analysis tools from Python libraries were then used to process and analyze the data before designing an appropriate predictor model. The predictor model is the central basis of the system for providing recommendations. The system process involves user profiling, data storage, and machine learning. Feedbacks help the system make an inference. The design of the algorithm of the recommendation process used a content-based filtering approach.")
    st.write("Analysis from ten columns was extracted from the raw dataset for prototyping; this included improving the dataset for efficient data processing through data cleaning. General attributes were reported, with each category being provided with a description. The research group then identified correlations between the respondent’s age and history of pregnancies revealing that most respondents had given birth ten years before their interview.  Furthermore, the analysis revealed that most respondents do not use modern contraceptives when mentioning family planning.")
    st.write("Incorporating modern methods such as recommender systems in SRH could increase awareness and acknowledgments for multiple individuals across the country. The system application will hopefully contribute to the proper and preferred use of modern contraceptives.")

    st.header('Background of the Study')
    st.write(
        "The Philippines has continued to rise in economic prowess. However, in terms of modern healthcare, the country still has much room for improvement in the health sector; sexual and reproductive health (SRH) is a department that needs improvement. Even with already established contraceptive methods being developed over the past years, there are still barriers in which individuals will encounter before even accessing any contraceptives—these range from income, political, and religious backgrounds [1].")
    st.write(
        "With laws and bills being passed to assist in SRH, such as the Responsible Parenthood and Reproductive Health Act of 2012 (RH law), the country continues to seek and improve programs and projects that help fulfill the needs of Filipinos in terms of SRH. One such program that has shown promising results is the Usapan program. The program introduces a behavioral approach by raising awareness of male responsibility for reproductive health under the Philippines' Family Planning Organization(FPOP).")
    st.write(
        "Even with established programs such as Usapan, most of the population would still refuse to apply modern contraceptive techniques, which would lead to the rapid growth of HIV cases and adolescent pregnancies[2]. In addition to this, the Philippines has only a 55 % prevalence rate on modern contraceptive use over the past decade. The consideration of existing behaviors and patterns of the preference of traditional contraceptive methods as opposed to modern methods is imperative to the study[3].")
    st.write(
        "Another group of researchers introduced the Systemic Anomalous Case Analysis method (SACA) to understand behaviors and existing research. SACA is a mixed-method approach to review existing research methods on the topic and compare and contrast the results to improve existing theories, measures, and experimental investigations on social phenomena relating to SRH [4].")
    st.write(
        "Additionally, the research itself provides a large amount of data and recorded interviews that span decades which can be utilized further into the study. Educational access to SRH has been taught in various ways, and each variety would yield different results [5].")
    st.write("Similar to the studies conducted by Sarah Jane Arcos Biton, the research results can be applied to existing strategies that can help in further advancing SRH education through campaign development and community seminars which additionally spreads more awareness on the topic.")
    st.write(
        'Implementing already existing technologies will also be considered. Examples of this are integrating smartphones and social media into a newly proposed healthcare system because of their relevance and impact among most of the population, especially for Family Planning (FP) and SRH. Furthermore, a high correlation between FP and smartphone ownership has been observed [6], thus further supporting integrating the technology into an SRH system.')
    st.write(
        'However, it is not smartphone usage alone that can affect contraceptive use and FP; social media is also another important factor in heightening awareness on the topic. The potential social media can assist in SRH is widely underused since there have not been more substantial studies conducted on the potential benefits of social media [7]. The overreliance on smartphones and social media can prove to benefit the research because of its level of necessity the user has towards it, especially among adolescents. Systematic reviews have been utilized to compare various mobile health (mHealth) tactics that have been applied to improve SRH awareness in lower-middle income countries [8].')
    st.write(
        'The trends of sexual health behavior, particularly in maternal and contraceptive health, among women in the age range of 15 to 24 in the Philippines indicate that targeted programs and policies are needed. A study by Juan, Laguna, and Pullum in 2019 concludes that young women in the Philippines were shown to have inconsistent knowledge and exposure to such information [9].')
    st.write(
        'Previous studies have used and developed sexual health information apps to increase sexual and reproductive health knowledge of its users [10, 11]. The studies were able to find that SRH apps are able to deliver sexual and reproductive health knowledge to its users [10].')
    st.write(
        "This lack of sexual health understanding and autonomy represents the need for policies and systems to be put in place as the lack of it increases the prevalence of immature pregnancies and births among the youth. In addition to that, the lack of education about oral or barrier contraceptive methods causes many women and girls to become fearful of potential side effects associated with these methods [7].")
    st.write("This study then intends to contribute to the decline of the trend of adolescent pregnancy, childbirth, sexual diseases among the youth in the Philippines, and encourage sex education through the creation of a recommender system targeted at maternal and contraceptive health. It intends to benefit existing technical solutions in Philippine healthcare regarding recommender systems by providing insight into how to approach maternal health and contraceptive health to prevent cases of early childbirth.")

    st.header('Research Gap')
    st.write("In solving the gap for a recommender system in the sub-area of maternal and contraceptive health, a part of the researchers' solution is to preprocess their collected data, design an appropriate model to determine existing trends and predictions, and apply it to a recommender system making use of artificial intelligence.")
    st.write('The researchers then hope that the outcomes of this study would be used for future recommender systems that will tackle other sub-areas of the broad medical field in the Philippines. Additionally, whilst it is proven that there is a deficiency in SRH access in terms of contraceptives, social stigmas, and religious/cultural backgrounds, there still exist drawbacks for contraceptive use. Current studies were able to show that there is a lack of knowledge in sexual reproductive and health knowledge in the Philippines')
    st.write(
        "Additionally, whilst it is proven that there is a deficiency in SRH access in terms of contraceptives, social stigmas, and religious/cultural backgrounds, there still exist drawbacks for contraceptive use. Current studies were able to show that there is a lack of knowledge in sexual reproductive and health knowledge in the Philippines[1, 3, 9]. ")
    st.write(
        'In addition, there were studies that aimed to address the lack of SRH knowledge; however, those studies were limited to certain demographic groups and no research was conducted for the Philippines [10, 11].')

    st.header('Objectives of the Study')
    st.write("In this regard, the study aims to target contraceptive and maternal health information specifically to create a recommender system. Specifically:")
    st.markdown(
        "- To analyze the 2017 DHS dataset for insights about SRH in the Philippines.")
    st.markdown("- To develop a prototype recommender system that predicts or recommends contraceptive information from a user's demographic data in tandem with existing literature on SRH and FP.")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:40px;
    }
    </style>
    ''', unsafe_allow_html=True)

    st.header('Significance of the Study')
    st.write(
        'Based on already existing frameworks, the group would analyze studies that relate to further improving SRH systems. In this case, examining an e-healthcare management framework applies recommender systems used to sustain health and disease interdiction and the default feature of analyzing user preferences [12, 13].')
    st.write(
        ' Moreover, fully realized recommender systems are able to reduce healthcare costs by a substantial fraction since a ‘similar-outcome low cost’ substitute would be presented to current medical practitioners during prescription can be integrated by clinicians through practice which could then conclude to a lower cost in healthcare [14].')

    st.header('Limitations')
    st.write('The broadness of existing recommender systems in healthcare primarily provides general results, as most of them aim to be a straightforward substitute for the proper diagnosis from a medical professional. Notably, with the increase of the audience for a particular recommender system, issues arise in its need for complexity to adapt to all sorts of expected and unexpected inputs.')
    st.write(
        "Healthcare systems that use recommenders will need to cope with imprecise terms (e.g., medical terms that have prefixes or suffixes), colloquial terms (e.g., the equivalence of medical terms to their layman's equivalent), and finally misspellings [15]. This problem is further heightened by the need to be assessed by several health experts regarding its use of vocabulary as descriptions of symptoms vary when other medical fields are involved in the system.")
    st.write("The study then focuses only on contraceptive and maternal health to limit these existing, occurring issues. Accordingly, it also fills in the problem for broad recommender systems, such that there is a lack of recommender systems in this specific sub-area of sexual health. A specific subcategory for a wide health-related field in sexual health allows the researchers to use mainly specific datasets to create and model a recommender system that only targets contraceptive and maternal health. ")

    st.header('Ethical Considerations')
    st.write('The research only considers legal and available contraceptive methods in the Philippines. It does not include outlawed emergency contraceptives (i.e., morning-after pills) used to prevent pregnancy following unprotected sexual intercourse or contraceptive failure. In turn, the contraceptives concerning morning-after pills will not be considered as a value when processing the data. ')

    st.header('References')
    st.write("""
    [1] Elia Gabarron and Rolf Wynn. 2016. Use of social media for sexual health promotion: a scoping review. Global Health Action ACM 9, 1. DOI: https://doi.org/10.3402/gha.v9.32193 
    \n[2] Sarah Jane Arcos Biton. 2020. Advancing sexual and reproductive health and rights: An overview of the best practices in the Philippines. Asian Journal of Women's Studies, ACM 26, 1, 114-127 pages. DOI: https://doi.org/10.1080/12259276.2019.1690778 
    \n[3] Maria Midea M. Kabamalan, Maria Paz N. Marques, and Elma P. Laguna. 2017. Ten Years of Traditional Contraceptive Method Use in the Philippines: Continuity and Change. ICF. 
    \n[4] Jessica D. Gipson, Jasmine Uysal, Subasri Narasimhan, and  Socorro (Connie) Gultiano. 2020. Using Systematic Anomalous Case Analysis to Examine Sexual and Reproductive Health Outcomes in the Philippines. Studies in Family Planning, ACM 51, 2, 21 pages. DOI: https://doi.org/10.1111/sifp.12115
    \n[5] Judith Odanee G. Magwilang, Eddieson Pasay-an, Petelyne P. Pangket. 2020. Knowledge, attitudes, and practices of adolescents regarding sexuality and reproductive issues in the Cordillera administrative region of the Philippines. Makara Journal of Health Research. ACM 24, 3. DOI: https://doi.org/10.7454/msk.v24i3.1245 
    \n[6] Apoorava Jadhav, & Julianne Weis. 2019. Mobile phone ownership, text messages, and contraceptive use: Is there a digital revolution in family planning?. Contraception. DOI: https://doi.org/10.1016/j.contraception.2019.10.004   
    \n[7] Olivia Rose Wood. 2020. Exploring Factors that Limit Contraception Use Among Adolescent Girls Aged 15-19 in Puerto Princesa, Palawan, Philippines. Colombia Academic Commons. Global Health Certificate, 4-15 pages. DOI: https://doi.org/10.7916/d8-cxme-6r43 
    \n[8] Farina Abrejo, Sumera Aziz Ali, Anam Feroz, Rozina Nuruddin & Sarah Saleem. 2019. Using mobile phones to improve young people’s sexual and reproductive health in low- and middle-income countries: a systematic review protocol to identify barriers, facilitators and reported interventions. Syst Rev. ACM 8, 117.  DOI: https://doi.org/10.1186/s13643-019-1033-5 
    \n[9] Christina P. Juan, Elma P. Laguna, and Thomas W. Pullum. 2019. Trends of Sexual and Reproductive Health Behaviors among Youth in the Philippines: Further Analysis of the 2008, 2013, and 2017 National Demographic and Health Surveys. DHS Further Analysis Reports No. 127. Rockville, Maryland, USA: ICF. https://www.dhsprogram.com/pubs/pdf/FA127/FA127.pdf. 
    \n[10] Lynae Brayboy, Alexandra Sepolen , Taylor Mezoian , Lucy Schultz , Benedict Landgren-Mills, Noelle Spencer, Carol Wheeler, Melissa Clark. 2017. Girl Talk: A Smartphone Application to Teach Sexual Health Education to Adolescent Girls. Journal of Pediatric & Adolescent Gynecology, 30, 1, 23-28. DOI:https://doi.org/10.1016/j.jpag.2016.06.011
    \n[11] Anna Nielsen, Aspasia Bågenholm, and Ayesha De Costa. 2020. Development of a Mobile Phone App to Promote Safe Sex Practice Among Youth in Stockholm, Sweden: Qualitative Study.  JMIR formative research, 4, 1, e12917. DOI:https://doi.org/10.2196/12917
    \n[12] Erni Astutik, Ferry Efendi, and Susy Katikana Sebayang. 2019. Women’s empowerment and the use of antenatal care services: analysis of demographic health surveys in five Southeast Asian countries. Women & Health, 1-17, 1155-1171 pages. DOI: https://doi.org/10.1080/03630242.2019.1593282 
    \n[13] P. Deepalakshmi and P. Nagaraj. 2020. A framework for e-healthcare management service using recommender system. Electronic Government, an International Journal 16, 1/2, 84-100 pages. DOI: https://doi.org/10.1504/EG.2020.105256 
    \n[14] Lina Bouayad, Balaji Padmanabhan, and Kaushal Chari. 2020. Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice. MIS Quarterly 44, 4, 1859-1903. DOI: https://doi.org/10.25300/MISQ/2020/14435  
    \n[15] Duygu Çelik Ertuğrul and Atilla Elçi. 2020. A survey on semanticized and personalized health recommender systems. Expert Systems 37, 4, 1-23. DOI:https://doi.org/10.1111/exsy.12519 """)
