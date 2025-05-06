FROM python:3.13.1
RUN apt-get -y update && apt-get -y install zlib1g-dev

EXPOSE 3000
WORKDIR /app

ENV PIPENV_VENV_IN_PROJECT=true
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PIPENV_SYSTEM=true

RUN pip install --upgrade pip 
RUN pip install pipenv

COPY Pipfile* /app/

RUN /usr/local/bin/pipenv sync

COPY src /app/src

ARG COMMIT_SHA=<not-specified>
RUN echo "mia_template_service_name_placeholder: $COMMIT_SHA" >> ./commit.sha

LABEL maintainer="%CUSTOM_PLUGIN_CREATOR_USERNAME%" \
      name="mia_template_service_name_placeholder" \
      description="%CUSTOM_PLUGIN_SERVICE_DESCRIPTION%" \
      eu.mia-platform.url="https://www.mia-platform.eu" \
      eu.mia-platform.language="Python" \
      eu.mia-platform.framework="FastAPI"

CMD ["python", "-m", "src.app"]