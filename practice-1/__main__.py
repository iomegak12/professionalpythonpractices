import crmsystem


def main():
    customerService = crmsystem.CustomerService()
    customers = customerService.getCustomers()

    for customer in customers:
        print("{}, {}, {}".format(customer["id"],
                                  customer["name"], customer["address"]))


if __name__ == "__main__":
    main()
