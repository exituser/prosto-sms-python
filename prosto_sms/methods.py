from . import models


class Methods:
    def __init__(self, data):
        self.request = data.request

    def push_message(
        self,
        *,
        text: str,
        phone: str,
        sender_name: str,
        priority: int = 2,
        external_id: str = None,
        route: str = None,
        call_protection: int = None
    ) -> models.PushMessageData:
        """
        Implementation of push_msg

        :param text: message text
        :param phone: receiver phone number
        :param sender_name: sender name
        :param priority: message priority
        :param external_id: ID in your platform
        :param route: message delivery route
        :param call_protection: call waiting time
        :return: result of calling the method
        """

        return models.PushMessageData(
            **self.request(
                method="push_msg",
                data={
                    "text": text,
                    "phone": phone,
                    "sender_name": sender_name,
                    "priority": priority,
                    "external_id": external_id,
                    "route": route,
                    "call_protection": call_protection
                }
            )
        )


    def get_message_report(
        self,
        *,
        id: int
    ) -> models.GetMessageReportData:
        """
        Implementation of

        :param id:
        :return: result of calling the method
        """

        return models.GetMessageReportData(
            **self.request(
                method="get_msg_report",
                data={
                    "id": id
                }
            )
        )

    def get_profile(self) -> models.GetProfileData:
        """
        Implementation of

        :return: result of calling the method
        """

        return models.GetProfileData(
            **self.request(
                method="get_profile"
            )
        )

    def get_prices(
        self,
        *,
        group_directions: int = None
    ) -> models.GetPricesData:
        """
        Implementation of

        :param group_directions:
        :return: result of calling the method
        """

        return models.GetPricesData(
            **self.request(
                method="get_prices",
                data={
                    "group_directions": group_directions
                }
            )
        )

    def wait_call(
        self,
        *,
        phone: str,
        call_protection: int
    ) -> models.WaitCallData:
        """
        Implementation of

        :param phone:
        :param call_protection:
        :return: result of calling the method
        """

        return models.WaitCallData(
            **self.request(
                method="wait_call",
                data={
                    "phone": phone,
                    "call_protection": call_protection
                }
            )
        )
