# EmoStream-Real-Time-Sentiment-Analysis-
# How to run
Run all these files in order in different terminals:<br>

1) sub_server
2) emoji_producer
3) spark_consumer
4) cluster
5) all the subscriber codes
6) emoji_client
7) monitor

In the emoji_client, when prompted add client_id, cluster_id and subscriber_id.



# Architecture

1) The sub_server sets a server at port 5002 its work is to store a the update value of subscriptions dictionary whenever a client is registered or deregister and sends this dictionary to the subscriber for pushing it to the respective clients under topic client_id
2) The emoji_client generates a list of random emojis and post it in the server 5001 and it also consumes the data it receives under the client_id
3) The emoji_producer receives the emoji in a queue from the server at port 5001 and pushes it to the spark engine every 2 seconds
4) The spark engine scales down the entire set of emoji according to the length of the emoji list and the main_publisher pushes it to the clusters under main_topic
5) The cluster receives the emoji and forwards it to the subscribers
6) Each subscriber of a particular clusters gets the list of clients connected to that subscriber from the sub_server an d pushes under the client_id
7) The kafka broker runs on server port 9092
