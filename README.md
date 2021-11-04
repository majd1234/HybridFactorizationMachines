# HybridFactorizationMachines
## Hybrid Music Recommendation Approach for Heterogeneous Information Network using Factorization Machines
When the recommendation model embeds user-item interactions, if we analyze the user preferences, we miss references to important content-based information or actual semantics of recommended items, which support the interpretation of a recommendation process. In this thesis, we will build a hybrid recommendation model based on content-based, context-based and collaborative filtering recommendation methods to leverage heterogeneous music information graph. To achieve this goal, a Music Information Knowledge Graph (MKG) is first constructed to encode different kinds of heterogeneous information, including the interactions between users, tracks and artists. Besides, we propose a hybrid music recommendation approach for MKG using factorization machines. Therefore, we propose a Content and Context-aware Hybrid Factorization Machine (CCaHFM) to train the recommendation models.

In the experimental part, we collect data from a wide and popular music platform called LastFM which contains a detailed profile of each user's musical taste and details of the tracks the user listens to. Moreover, we extend our dataset to be more effective by involving data about the content characteristic of the collected tracks (tracks content data) and the artists who sing these tracks (artists context data). Therefore, we get the content characteristic of the tracks from Spotify and we collect the artist details from DBpedia. Finally, all these data resources are integrated into MKG.
Building Hybrid recommender based on MKG and factorization machines techniques shows that dealing with relevant content and context information can be used to increase the recommendation accuracy and to improve the awareness of the reasons behind user's preferences.

The experiments in this thesis are conducted to prove the importance of CCaHFM in improving the recommendation system by understanding and analyzing the user profiles based on the historical data of user preferences with the content and context features we have.

## Reference
The knowledge-aware hybrid factorization machines (kaHFM) proposed by the citation below is the main work this thesis borrows from. The authors in this paper initialize latent factors in factorization machines by using semantic features which exist in knowledge graph nodes in order to train an interpretable model. Our contribution in this thesis will extend the factorization machines towards a different kind of features in the field of music. 

### The article citation: 
Vito Walter Anelli, Tommaso Di Noia, Eugenio Di Sciascio, Azzurra Ragone, Joseph Trotta: How to Make Latent Factors Interpretable by Feeding Factorization Machines with Knowledge Graphs. ISWC (1) 2019: 38-56. URL:  https://link.springer.com/chapter/10.1007%2F978-3-030-30793-6_3.

## Credit
This recommendation model has been developed by Dipl.-Ing. Majd Azzam while under the supervision of Univ.-Prof. Mag. Dipl.-Ing. Dr. Markus Schedl at the institute for Computational Perception at Johannes Kepler Universität Linz | JKU Linz.

## Contact
Majdazzam111@gmail.com
