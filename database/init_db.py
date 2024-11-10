from py2neo import Graph

class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__graph = None
        try:
            # Set up an in-memory Neo4j database
            self.__graph = Graph(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        # No explicit close needed for py2neo, but this can be used for cleanup
        self.__graph = None

    def query(self, query, parameters=None):
        # assert self.__driver is not None, "Graph not initialized!"
        assert self.__graph is not None, "Graph not initialized!"
        response = None
        try:
            response = list(self.__graph.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
        return response

    # Function to create a user
    def create_user(self, username, password, email=None):
        return self.query(
            "CREATE (u:User {username: $username, password: $password, email: $email}) RETURN u",
            parameters={"username": username, "password": password, "email": email}
        )

    # Function to authenticate a user
    def authenticate_user(self, username, password):
        result = self.query(
            "MATCH (u:User {username: $username, password: $password}) RETURN u",
            parameters={"username": username, "password": password}
        )
        return result[0] if result else None

    # Function to store itinerary history
    def save_itinerary(self, username, itinerary):
        return self.query(
            """
            MATCH (u:User {username: $username})
            CREATE (u)-[:HAS_HISTORY]->(i:Itinerary {details: $itinerary})
            RETURN i
            """,
            parameters={"username": username, "itinerary": itinerary}
        )






# from neo4j import GraphDatabase

# class Neo4jConnection:
#     def __init__(self, uri, user, pwd):
#         self.__uri = uri
#         self.__user = user
#         self.__pwd = pwd
#         self.__driver = None
#         try:
#             self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
#         except Exception as e:
#             print("Failed to create the driver:", e)

#     def close(self):
#         if self.__driver is not None:
#             self.__driver.close()

#     def query(self, query, parameters=None):
#         assert self.__driver is not None, "Driver not initialized!"
#         session = None
#         response = None
#         try:
#             session = self.__driver.session()
#             response = list(session.run(query, parameters))
#         except Exception as e:
#             print("Query failed:", e)
#         finally:
#             if session is not None:
#                 session.close()
#         return response

#     # Function to create a user
#     def create_user(self, username, password, email=None):
#         return self.query(
#             "CREATE (u:User {username: $username, password: $password, email: $email}) RETURN u",
#             parameters={"username": username, "password": password, "email": email}
#         )

#     # Function to authenticate a user
#     def authenticate_user(self, username, password):
#         result = self.query(
#             "MATCH (u:User {username: $username, password: $password}) RETURN u",
#             parameters={"username": username, "password": password}
#         )
#         return result[0] if result else None

#     # Function to store itinerary history
#     def save_itinerary(self, username, itinerary):
#         return self.query(
#             """
#             MATCH (u:User {username: $username})
#             CREATE (u)-[:HAS_HISTORY]->(i:Itinerary {details: $itinerary})
#             RETURN i
#             """,
#             parameters={"username": username, "itinerary": itinerary}
#        )


# from neo4j import GraphDatabase

# class Neo4jConnection:
#     def __init__(self, uri, user, pwd):
#         self.__uri = uri
#         self.__user = user
#         self.__pwd = pwd
#         self.__driver = None
#         try:
#             self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
#         except Exception as e:
#             print("Failed to create the driver:", e)

#     def close(self):
#         if self.__driver is not None:
#             self.__driver.close()

#     def query(self, query, parameters=None):
#         assert self.__driver is not None, "Driver not initialized!"
#         session = None
#         response = None
#         try:
#             session = self.__driver.session()
#             response = list(session.run(query, parameters))
#         except Exception as e:
#             print("Query failed:", e)
#         finally:
#             if session is not None:
#                 session.close()
#         return response
