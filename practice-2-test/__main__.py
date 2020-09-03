from injector import Injector
from crmsystem import TableGenerator, CRMSystemError, \
    CRMSystemServiceController, CustomerService, OrderService


def main():
    def configure(binder):
        binder.bind(CustomerService,
                    to=CustomerService(lambda customers:
                                       print(TableGenerator.get_customer_table(customers))))
        binder.bind(OrderService,
                    to=OrderService(lambda orders:
                                    print(TableGenerator.get_orders_table(orders))))

    try:
        injector = Injector([configure])
        controller = injector.get(CRMSystemServiceController)

        if controller is None:
            raise Exception("Invalid Controller Impl Specified")

        controller.process(lambda: print(
            'Both Services Completed Their Operations ...'))
    except CRMSystemError as error:
        print('Application Error Occurred ... {0}'.format(error.__str__()))
    except Exception as error:
        print('General Error Occurred!')
    except:
        print('Unknown Error Occurred!')


if __name__ == "__main__":
    main()
