from django.http import HttpResponseGone


def gone(request):
    apiv0_gone_msg = """APIv0 was removed on January 31, 2016. Please switch to APIv1:
                        <ul>
                            <li>
                                <a href="/api/v1/">APIv1 Endpoint</a>
                            </li>
                            <li>
                                <a href="/apiv1_docs/">APIv1 Documentation</a>
                            </li>
                            <li>
                                <a href="/apiv0_shutdown/">APIv0 shut down notice</a>
                            </li>
                        </ul>
                        """
    return HttpResponseGone(apiv0_gone_msg)
