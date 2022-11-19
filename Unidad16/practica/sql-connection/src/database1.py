import sqlalchemy as db

class Database():
    """Handler of Customer table in database
    """

    engine = db.create_engine("postgresql://postgres:Pa$$w0rd@localhost:5432/test")

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB instance create")

    
    def get_table(self, query):
        """returns an entire table
        :param query: Name table
        :type query: str
        """
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery:
            print(data)


        """Insert a customer in a table
        :param customer: customer to save
        :type customer: Customer
        """
        self.connection.execute(f"""INSERT INTO customer( name, age, email, address, zip_code)
                                    VALUES('{customer.name}',
                                            '{customer.age}',
                                            '{customer.email}',
                                            '{customer.address}',
                                            '{customer.zip_code}')""")

    
    def fetchByName(self):
        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchCustomerById(self, customer_id):
        """get customer by id
        :param customer_id: customer id
        :type customer_id: int
        """
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.id ==customer_id)
        return customerData

    # Create Customer
    def save_data(self, customer):
        """method to save a client with incomplete information
        :param customer: customer with incomplete information
        :type customer: Customer
        """
        session = Session(bind=self.connection)
        session.add(customer)
        session.commit()

    # Update Customer
    def updateCustomer(self, customerName, address):
        """Update customer address based on the name
        :param customerName: customer name
        :type customerName: str
        :param address: customer address
        :type queaddressry: str
        """
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        customerData = session.query(Customer).filter(Customer.name ==customerName)
        customerData.update(dataToUpdate)
        session.commit()

    # Delete Customer
    def deleteCustomer(self, customer_id):
        """delete customer based on the id
        :param customer_id: customer id
        :type customer_id: int
        """
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.id ==customer_id).first()
        session.delete(customerData)
        session.commit()