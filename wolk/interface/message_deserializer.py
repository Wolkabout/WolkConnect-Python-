"""Process messages received from WolkAbout IoT Platform."""
#   Copyright 2018 WolkAbout Technology s.r.o.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from wolk.model.actuator_command import ActuatorCommand
from wolk.model.configuration_command import ConfigurationCommand
from wolk.model.message import Message
from wolk.model.file_transfer_package import FileTransferPackage


class MessageDeserializer(metaclass=ABCMeta):
    """Deserialize messages received from the platform."""

    def __init__(self, inbound_topics: List[str]):
        """
        Set inbound topics for device.

        :param inbound_topics: List of topics to subscribe to
        :type inbound_topics: List[str]
        """
        self.inbound_topics = inbound_topics

    @abstractmethod
    def is_actuation_command(self, message: Message) -> bool:
        """
        Check if message is actuation command.

        :param message: The message received
        :type message: Message
        :returns: actuation_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_configuration_command(self, message: Message) -> bool:
        """
        Check if message is configuration command.

        :param message: The message received
        :type message: Message
        :returns: configuration_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_firmware_install(self, message: Message) -> bool:
        """
        Check if message is firmware update install command.

        :param message: The message received
        :type message: Message
        :returns: firmware_update_install_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_firmware_abort(self, message: Message) -> bool:
        """
        Check if message is firmware update command.

        :param message: The message received
        :type message: Message
        :returns: firmware_update_abort_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_binary_response(self, message: Message) -> bool:
        """
        Check if message is file binary message.

        :param message: The message received
        :type message: Message
        :returns: file_binary_response
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_delete_command(self, message: Message) -> bool:
        """
        Check if message if file delete command.

        :param message: The message received
        :type message: Message
        :returns: file_delete_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_purge_command(self, message: Message) -> bool:
        """
        Check if message if file purge command.

        :param message: The message received
        :type message: Message
        :returns: file_purge_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_list_confirm(self, message: Message) -> bool:
        """
        Check if message is file list confirm.

        :param message: The message received
        :type message: Message
        :returns: file_list_confirm
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_list_request(self, message: Message) -> bool:
        """
        Check if message is file list request.

        :param message: The message received
        :type message: Message
        :returns: file_list_request
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_upload_initiate(self, message: Message) -> bool:
        """
        Check if message is file upload command.

        :param message: The message received
        :type message: Message
        :returns: file_upload_initiate_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_upload_abort(self, message: Message) -> bool:
        """
        Check if message is file upload command.

        :param message: The message received
        :type message: Message
        :returns: file_upload_abort_command
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_url_initiate(self, message: Message) -> bool:
        """
        Check if message is file URL download command.

        :param message: The message received
        :type message: Message
        :returns: file_url_download_initiate
        :rtype: bool
        """
        pass

    @abstractmethod
    def is_file_url_abort(self, message: Message) -> bool:
        """
        Check if message is file URL download command.

        :param message: The message received
        :type message: Message
        :returns: file_url_download_abort
        :rtype: bool
        """
        pass

    @abstractmethod
    def parse_actuator_command(self, message: Message) -> ActuatorCommand:
        """
        Parse the message into an ActuatorCommand.

        :param message: The message received
        :type message: Message
        :returns: actuation
        :rtype: ActuatorCommand
        """
        pass

    @abstractmethod
    def parse_firmware_install(self, message: Message) -> str:
        """
        Return file name from message.

        :param message: The message received
        :type message: Message
        :returns: file_name
        :rtype: str
        """
        pass

    @abstractmethod
    def parse_file_initiate(self, message: Message) -> Tuple[str, int, str]:
        """
        Return file name, file size and file hash from message.

        :param message: The message received
        :type message: Message
        :returns: (file_name, file_size, file_hash)
        :rtype: Tuple[str, int, str]
        """
        pass

    @abstractmethod
    def parse_file_url(self, message: Message) -> str:
        """
        Parse the message into a URL string.

        :param message: The message received
        :type message: Message
        :returns file_url:
        :rtype: str
        """
        pass

    @abstractmethod
    def parse_file_binary(self, message: Message) -> FileTransferPackage:
        """
        Parse the message into a file transfer package.

        :param message: The message received
        :type message: Message
        :returns: file_transfer_package
        :rtype: FileTransferPackage
        """
        pass

    @abstractmethod
    def parse_configuration(self, message: Message) -> ConfigurationCommand:
        """
        Parse the message into a ConfigurationCommand.

        :param message: The message received
        :type message: Message
        :returns: configuration
        :rtype: ConfigurationCommand
        """
        pass

    @abstractmethod
    def parse_file_delete_command(self, message: Message) -> str:
        """
        Parse the message into a file name to delete.

        :param message: The message received
        :type message: Message
        :returns: file_name
        :rtype: str
        """
        pass
